package com.hybrid.framework.locators;
import static com.hybrid.framework.execution.Execution.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;

public class XpathLocator {
	

	// Re-usability of xpath element
	public static WebElement getXpathElement(String xpath){
		
		try{
		WebDriverWait Ww = new WebDriverWait(driver, 45);
		
		return Ww.until(ExpectedConditions.visibilityOfElementLocated(((By.xpath(xpath)))));
		}catch(Exception e){
			
			
		}
		return null;
	}
	
}
