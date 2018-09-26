package com.hybrid.framework.locators;
import jxl.write.WriteException;
import jxl.write.biff.RowsExceededException;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import com.hybrid.framework.execution.Execution;


public class SpecialFunctions {

	// Re-usability of xpath element
	public static void scrollelementview(String xpath) throws RowsExceededException, WriteException, InterruptedException 	{
		WebElement element = Execution.driver.findElement(By.xpath(xpath));
		((JavascriptExecutor) Execution.driver).executeScript("arguments[0].scrollIntoView(true);", element);
		}
	public static void end(String xpath)	{
		Execution.driver.findElement(By.xpath(xpath)).sendKeys(Keys.END);
		
		}
	
	public static void rightArrow(String xpath, String values) throws InterruptedException{
        for (int i = 0; i < Integer.valueOf(values); i++){
        Execution.driver.findElement(By.xpath(xpath)).sendKeys(Keys.ARROW_RIGHT);
         //wait 200 milli second
          Thread.sleep(200);
        } }

}