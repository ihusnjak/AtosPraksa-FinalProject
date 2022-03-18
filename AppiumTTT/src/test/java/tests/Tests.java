package tests;

import org.testng.Assert;
import org.testng.annotations.Test;

import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.Status;

import io.appium.java_client.MobileElement;
import io.appium.java_client.android.StartsActivity;

public class Tests extends BaseClass {

	@Test()
	public void test0() {
		// creates a toggle for the given test, adds all log events under it
		ExtentTest testCreateSession = extent.createTest("Create session", "test if session is created");
		// log(Status, details)
		testCreateSession.log(Status.INFO, "Create session test started");
		String activity = ((StartsActivity) driver).currentActivity();
		testCreateSession.log(Status.PASS, "Obtaining current activity");
		String pkg = ((StartsActivity) driver).getCurrentPackage();
		testCreateSession.log(Status.PASS, "Obtaining current package");
		Assert.assertEquals(activity, ".Calculator");
		Assert.assertEquals(pkg, "com.android.calculator2");
		testCreateSession.log(Status.INFO, "Create session test completed");
	}

	@Test
	public void test1() {
		ExtentTest test1 = extent.createTest("Test 5+5", "test if 5+5=10");
		test1.log(Status.INFO, "Test 5+5 started");
		MobileElement el1 = (MobileElement) driver.findElementById("com.android.calculator2:id/digit_5");
		el1.click();
		test1.log(Status.PASS, "Digit 5 clicked");
		MobileElement el2 = (MobileElement) driver.findElementByAccessibilityId("plus");
		el2.click();
		test1.log(Status.PASS, "Plus clicked");
		MobileElement el3 = (MobileElement) driver.findElementById("com.android.calculator2:id/digit_5");
		el3.click();
		test1.log(Status.PASS, "Digit 5 clicked");
		MobileElement el4 = (MobileElement) driver.findElementByAccessibilityId("jednako");
		el4.click();
		test1.log(Status.PASS, "Equals clicked");
		String strRes = driver.findElementById("com.android.calculator2:id/result").getText();
		System.out.println("\nResult is : " + strRes);
		String expRes = "10";
		Assert.assertEquals(strRes, expRes);
		test1.log(Status.INFO, "Test 5+5 completed");

	}

	@Test
	public void test2() {
		ExtentTest test1 = extent.createTest("Test 4+3", "test if 4+3=7");
		test1.log(Status.INFO, "Test 4+3 started");
		MobileElement el1 = (MobileElement) driver.findElementById("com.android.calculator2:id/digit_4");
		el1.click();
		test1.log(Status.PASS, "Digit 4 clicked");
		MobileElement el2 = (MobileElement) driver.findElementByAccessibilityId("plus");
		el2.click();
		test1.log(Status.PASS, "Plus clicked");
		MobileElement el3 = (MobileElement) driver.findElementById("com.android.calculator2:id/digit_3");
		el3.click();
		test1.log(Status.PASS, "Digit 3 clicked");
		MobileElement el4 = (MobileElement) driver.findElementByAccessibilityId("jednako");
		el4.click();
		test1.log(Status.PASS, "Equals clicked");
		String strRes = driver.findElementById("com.android.calculator2:id/result").getText();
		System.out.println("\nResult is : " + strRes);
		String expRes = "7";
		Assert.assertEquals(strRes, expRes);
		test1.log(Status.INFO, "Test 4+3 completed");

	}

	@Test
	public void test3() {
		ExtentTest test1 = extent.createTest("Test 9-4", "test if 9-4=5");
		test1.log(Status.INFO, "Test 9-4 started");
		MobileElement el1 = (MobileElement) driver.findElementById("com.android.calculator2:id/digit_9");
		el1.click();
		test1.log(Status.PASS, "Digit 9 clicked");
		MobileElement el2 = (MobileElement) driver.findElementByAccessibilityId("minus");
		el2.click();
		test1.log(Status.PASS, "Minus clicked");
		MobileElement el3 = (MobileElement) driver.findElementById("com.android.calculator2:id/digit_4");
		el3.click();
		test1.log(Status.PASS, "Digit 4 clicked");
		MobileElement el4 = (MobileElement) driver.findElementByAccessibilityId("jednako");
		el4.click();
		test1.log(Status.PASS, "Equals clicked");
		String strRes = driver.findElementById("com.android.calculator2:id/result").getText();
		System.out.println("\nResult is : " + strRes);
		String expRes = "5";
		Assert.assertEquals(strRes, expRes);
		test1.log(Status.INFO, "Test 9-4 completed");

	}

	// this was used in testing Chrome driver ....
	// @Test
	// public void testChrome() {
	// driver.get("https://google.com");
	// driver.findElement(By.name("q")).sendKeys("Appium");
	// driver.findElement(By.name("q")).sendKeys(Keys.ENTER);
	// System.out.println("Test finished...");

	// }

}
