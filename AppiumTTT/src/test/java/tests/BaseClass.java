package tests;

import java.net.URL;

import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.remote.MobileCapabilityType;

public class BaseClass extends ExtentReportsForTTT{

	AppiumDriver<MobileElement> driver;

	@BeforeTest
	public void setup() {

		try {
			DesiredCapabilities caps = new DesiredCapabilities();

			// caps.setCapability("platformName", "android");
			// if we dont know capability "key" pair (name) we can use CapabilityType
			// interface
			// code below is the same as "platformName", "android"

			caps.setCapability(MobileCapabilityType.PLATFORM_NAME, "android");
			caps.setCapability(MobileCapabilityType.PLATFORM_VERSION, "6.0");
			caps.setCapability(MobileCapabilityType.DEVICE_NAME, "HTC One_M8");
			caps.setCapability(MobileCapabilityType.UDID, "HT465WM05566");
			caps.setCapability(MobileCapabilityType.NEW_COMMAND_TIMEOUT, 30);
			
			//caps.setCapability(MobileCapabilityType.BROWSER_NAME, "Chrome");
			
			caps.setCapability("appPackage", "com.android.calculator2");
			caps.setCapability("appActivity", "com.android.calculator2.Calculator");
			
			//caps.setCapability(MobileCapabilityType.BROWSER_NAME, "CHROME");
			// will use abs. path with .apk in apps folder later
			// caps.setCapability(MobileCapabilityType.APP, "");

			URL url = new URL("http://127.0.0.1:4723/wd/hub");
			driver = new AndroidDriver<MobileElement>(url, caps);
			
			
			
			//we can use AppiumDriver too (AndroidDriver extends AppiumDriver )
			//driver = new AppiumDriver<MobileElement>(url, caps);
			
		} catch (Exception e) {
			System.out.println("Cause: " + e.getCause());
			System.out.println("Message: " + e.getMessage());
			e.printStackTrace();
		}

	}

	
	@AfterTest
	public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

}
