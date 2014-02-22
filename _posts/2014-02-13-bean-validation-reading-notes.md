---
layout: post
title: "Bean Validation JSR-303 阅读笔记"
description: "Bean Validation JSR-303 阅读笔记"
category: Coding
tags: [Java, JSR-303]
---

# Bean Validation JSR-303 阅读笔记

## 1. Constraint Definition 约束定义

约束是由一系列的约束注解 **Contraint annotation** 和一系列的约束校验器实现 **Contraint validation implementations** 组成的。

### 1.1 Contraint Annotation 约束注解

JavaBean中的一个注解通过一个或多个约束注解来表达。一个约束注解是`retention policy`为 `RUNTIME` 并被 `javax.validation.Contraint`注解的注解。

让我们来创建一个新的用来判断一个给定字符串是否全是大写或者小写字符的约束标注。

首先,我们需要一种方法来表示这两种模式( 译注: 大写或小写), 我们可以使用String常量, 但是在Java 5中, 枚举类型是个更好的选择:

{% highlight java %}
    package pw.yougang;
    
    public enum CaseMode {
        UPPER, LOWER;
    }{% endhighlight %}
然后让我们来创建一个生命约束条件的 **Annotation**

{% highlight java %}
    @Target({ METHOD, FIELD, ANNOTATION_TYPE })
    @Retention(RUNTIME)
    @Constraint(validatedBy = CheckCaseValidator.class)
    @Documented
    public @interface CheckCase {
    	String message() default "{com.mycompany.constraints.checkcase}";
    
    	Class<?>[] groups() default {};
    
    	Class<? extends Payload>[] payload() default {};
    
    	CaseMode value();
    }
{% endhighlight %}

- `@Target({ METHOD, FIELD, ANNOTATION_TYPE })` 表示这个Annotation可以用来修饰方法，字段和其他注解
- `@Retention(RUNTIME)` 表示这个Annotation 的检查期运行期，这是JSR-303的强制规定
-  `@Constraint(validatedBy = CheckCaseValidator.class) ` JSR-303规定一个 **Constraint Annotation** 需要具有一个对应的约束校验器 **Constraint Validator** ，通过对约束规则增加 `@Constraint` 注解，并设置属性 `validatedBy` 指定对应的约束校验器
-  JSR-303 强制性的规定了在注解中必须实现的3个属性： 分别是 `message`: 指定校验失败时的信息；`groups` 指定分组；`payload` 元数据信息，通常用来表示校验失败时的严重程度。
-  其他属性都是自定义的了，在这里我们定义了一个表示大小或小写的枚举成员 value

### 1.2 约束校验器

在1.1中我们提到了，一个约束注解是与一个约束校验器绑定的；只有通过约束校验器才能完成校验的动作。

下面是`CheckCase`的校验器

{% highlight java %}
    package com.mycompany;
    
    import javax.validation.ConstraintValidator;
    import javax.validation.ConstraintValidatorContext;
    
    public class CheckCaseValidator implements
    		ConstraintValidator<CheckCase, String> {
    
    	private CaseMode caseMode;
    	private CheckCase annotation;
    
    	public void initialize(CheckCase constraintAnnotation) {
    		this.caseMode = constraintAnnotation.value();
    		this.annotation = constraintAnnotation;
    	}
    
    	public boolean isValid(String value, ConstraintValidatorContext context) {
    		if (value == null) {
    			return true;
    		}
    
    		boolean isValid;
    
    		if (caseMode == CaseMode.UPPER) {
    			isValid = value.equals(value.toUpperCase());
    		} else {
    			isValid = value.equals(value.toLowerCase());
    		}
    
    		if (!isValid) {
    			context.disableDefaultConstraintViolation();
    			context.buildConstraintViolationWithTemplate(
    					this.annotation.message()).addConstraintViolation();
    		}
    		return isValid;
    	}
    
    }

{% endhighlight %}
- 所有的约束校验器必须实现`ConstraintValidator<ConstraintAnnotation, T>` 接口，这里同时指定了2个泛型参数，第一个对应相应的Annotation，第二个是指待校验的数据类型。对于这个T具有2个约束，1. 必须为 non parameterized type，就是不接受泛型参数的类型 ；2. 如果接受泛型参数，那么只允许接受`？`。
    
    {% highlight java %}
       // 合法的声明
       ... implements ConstraintValidator<CheckCase, String>
       
       // 合法的声明 
       ... implements ConstraintValidator<CheckCase, Collection>
       
       // 合法的声明
        ... implements ConstraintValidator<CheckCase, Collection<?>>
        
        //不合法的声明
         ... implements ConstraintValidator<CheckCase, Collection<String>>
    {% endhighlight %}
    
- 接口中的2个方法 `public void initialize(CheckCase constraintAnnotation) ;` 该方法会被`ValidatorFactory`实例化校验器时调用，传递相应的注解信息；
- `public boolean isValid(String value, ConstraintValidatorContext context);` 该方法是我们重点要关注的了

在JSR-303中，建议在 `isValid` 中将 **NULL** 值的校验和该校验器的校验分开。NULL通过 `@NotNull` 校验去去校验。基本就是让你不要去管Null的意思，如果是Null就直接返回 `true` 吧。

- `context.buildConstraintViolationWithTemplate(
    					this.annotation.message()).addConstraintViolation();` 校验结果推荐通过`ConstraintViolation` 来传递。这会把所有的校验错误放到一个Set里面，方便 `Validation API` 统一处理错误信息。在这里我们用了 Template， 基本就是可以把`Annotation` 中设定的值通过模板表示，可参看注解定义中的message "Case {value}." 部分。最后记得必须调用 `addConstraintViolation()` 不然，是加入不到队列里面的。
    					
### 1.3 Validation API & TestCase

最后列一个 `TestCase`

{% highlight java %}
    package com.mycompany;
    
    public class Car {
    
    	private String manufacturer;
    
    	@CheckCase(CaseMode.UPPER)
    	private String licensePlate;
    
    	private int seatCount;
    
    	public Car(String manufacturer, String licencePlate, int seatCount) {
    		this.manufacturer = manufacturer;
    		this.licensePlate = licencePlate;
    		this.seatCount = seatCount;
    	}
    
    	public String getManufacturer() {
    		return manufacturer;
    	}
    
    	public void setManufacturer(String manufacturer) {
    		this.manufacturer = manufacturer;
    	}
    
    	public String getLicensePlate() {
    		return licensePlate;
    	}
    
    	public void setLicensePlate(String licensePlate) {
    		this.licensePlate = licensePlate;
    	}
    
    	public int getSeatCount() {
    		return seatCount;
    	}
    
    	public void setSeatCount(int seatCount) {
    		this.seatCount = seatCount;
    	}
    }
    
    package com.mycompany;

    import static org.junit.Assert.assertEquals;
    
    import java.util.Set;
    
    import javax.validation.ConstraintViolation;
    import javax.validation.Validation;
    import javax.validation.Validator;
    import javax.validation.ValidatorFactory;
    
    import org.junit.BeforeClass;
    import org.junit.Test;
    
    public class CarTest {
    
    	private static Validator validator;
    
    	@BeforeClass
    	public static void setUp() {
    		ValidatorFactory factory = Validation.buildDefaultValidatorFactory();
    		validator = factory.getValidator();
    	}
    
    	@Test
    	public void testLicensePlateNotUpperCase() {
    		Car car = new Car("Morris", "dd-ab-123", 4);
    		Set<ConstraintViolation<Car>> violations = validator.validate(car);
    		assertEquals(1, violations.size());
    		assertEquals("Case mode must be UPPER.", violations.iterator().next()
    				.getMessage());
    	}
    }
{% endhighlight %}

收工。。。