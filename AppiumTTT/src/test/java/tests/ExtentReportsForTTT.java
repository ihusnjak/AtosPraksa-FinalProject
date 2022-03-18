package tests;

import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;

public class ExtentReportsForTTT {

	ExtentSparkReporter spark;
	ExtentReports extent;

	@BeforeSuite
	public void reportSetup() {
		
		// start reporter
		spark = new ExtentSparkReporter("TTTReport.html");
		spark.config().setReportName("Calculator automation demo");
		spark.config().setTimeStampFormat("xs_ms_nz");

		// create ExtentReports and attach reporter(s)
		extent = new ExtentReports();
		extent.attachReporter(spark);

	}

	@AfterSuite
	public void ReportTearDown() {
		// calling flush writes everything to the log file
		extent.flush();
	}

}
