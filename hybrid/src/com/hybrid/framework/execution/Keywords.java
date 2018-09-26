package com.hybrid.framework.execution;

import static com.hybrid.framework.reports.Reports.*;
import static com.hybrid.framework.execution.Execution.*;
import static com.hybrid.framework.reports.TimeTaken.*;
import static com.hybrid.framework.locators.XpathLocator.*;
import static com.hybrid.framework.reports.Screenshot.*;
import org.openqa.selenium.JavascriptExecutor;
import java.io.IOException;
import java.util.Date;

import jxl.write.WriteException;
import org.openqa.selenium.Keys;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.Point;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.remote.RemoteWebDriver;
//import org.openqa.selenium.remote.server.handler.interactions.touch.Scroll;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
//import org.openqa.selenium.*;

import com.google.common.base.Function;
import com.hybrid.framework.locators.SpecialFunctions;
import com.hybrid.framework.locators.XpathLocator;
//import com.thoughtworks.selenium.Wait;

public class Keywords {
	
	
	public static WebDriverWait wait = new WebDriverWait(driver, 25);
	
	public static void keyword(String actionContent,String xpath,String value, String expected, int statusRow, int reportStatus) throws WriteException, IOException, InterruptedException{
		
		String startTimes = sdf.format(new Date().getTime());
		String endTimes =null;

		try{			
			
		switch(actionContent.toLowerCase()){
		
		
		case "click":
			try{
				
	
			getXpathElement(xpath).click();
			endTimes = sdf.format(new Date().getTime());
			
			setXLValues("objects", 9, statusRow, "Pass");	
			setReports("objects", 12, reportStatus, "Element clicked");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));
			
			} catch (Exception e){
				
				endTimes = sdf.format(new Date().getTime());
				setXLValues("objects", 9, statusRow, "Fail");
				setReports("objects", 12, reportStatus, "Element not clicked");
				setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

				
			}
			
			break;
		case "Horizontal":
			JavascriptExecutor jsx = (JavascriptExecutor) driver;
			jsx.executeScript("window.scrollBy(-95,0)", "");
			String elementId = "element-id";
			String html =(String) jsx.executeScript("return document.getElementById('" + elementId + "').innerHTML;");
			break;
		
		case "presence":
            try{
                
                if(wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(xpath))).isDisplayed()){
                endTimes = sdf.format(new Date().getTime());                
                setXLValues("objects", 9, statusRow, "Pass");
                setReports("objects", 12, reportStatus, "Element Present");
                setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));
                }               
                }
    catch (Exception e) {
                    endTimes = sdf.format(new Date().getTime());                
                    setXLValues("objects", 9, statusRow, "Fail");
                    setReports("objects", 12, reportStatus, "Element Not Present");
                    setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));           
                    getScreenshot(xpath);
                    
                }    
            
            break;		
		
		case "scrolldown":
			
		 for (int second = 0;; second++) {
		           if(second >=Integer.valueOf(value)){
		               break;
		           }
		       ((RemoteWebDriver) driver).executeScript("window.scrollBy(0,200)", "");
		               Thread.sleep(300);
		 }
		 break;
		
		case "scrollup":
			
			 for (int second = 0;; second++) {
			           if(second >=Integer.valueOf(value)){
			               break;
			           }
			       ((RemoteWebDriver) driver).executeScript("window.scrollBy(200,0)", "");
			               Thread.sleep(300);
			 }
			 break;
			 
		case "sleep":
            Thread.sleep(Integer.parseInt(value));
            
            break;
			
       case "Escape":    
            
            
            try{
                
                Execution.driver.findElement(By.xpath(xpath)).sendKeys(Keys.ESCAPE);
                endTimes = sdf.format(new Date().getTime());             
                setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));             
                }
            catch (Exception e) {
                    endTimes = sdf.format(new Date().getTime());                    
                    setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));
                    
                }
            break;
		 
	/*	case "focus":
			try{
			JavascriptExecutor jsx1 = (JavascriptExecutor) driver;
		//	String elementId = "element-id";
			String html =(String) jsx.executeScript("return document.getElementByXpath('" + xpath + "').innerHTML;");
			setXLValues("objects", 9, statusRow, "Pass");	
			setReports("objects", 12, reportStatus, "Focused");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

			}
			 catch (Exception e){
			        setXLValues("objects", 9, statusRow, "Fail");
					setReports("objects", 12, reportStatus, "Not Focused");
					setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));
		
				}	
	break;
	*/
		
		case "enter":
			try{
				
			getXpathElement(xpath).sendKeys(value);
			endTimes = sdf.format(new Date().getTime());

			setXLValues("objects", 9, statusRow, "Pass");
			setReports("objects", 12, reportStatus, "Elements entered");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));


			}catch (Exception e) {
				endTimes = sdf.format(new Date().getTime());

				setXLValues("objects", 9, statusRow, "Fail");
				setReports("objects", 12, reportStatus, "Elements not entered");
				setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

				getScreenshot(xpath);
				
			}
			
			break;
		
		case "pagedown":    
            driver.findElement(By.xpath(xpath)).sendKeys(Keys.PAGE_DOWN);
            driver.findElement(By.xpath(xpath)).sendKeys(Keys.PAGE_DOWN);

            break;
		
		case "checkcontent":
			

			String actual = getXpathElement(xpath).getText();
			
			endTimes = sdf.format(new Date().getTime());

			
			if(actual.equals(expected)){
			setXLValues("objects", 9, statusRow, "Pass");
			setXLValues("objects", 7, statusRow, actual);
			setReports("objects", 12, reportStatus, "Content matched");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

			}else 
			{
			
			endTimes = sdf.format(new Date().getTime());

			setXLValues("objects", 9, statusRow, "Fail");
			setXLValues("objects", 7, statusRow, actual);
			setReports("objects", 12, reportStatus, "Contents mismatched");		
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

			}
			break;
     
		case "getText":
			
			try{

			String actual1 = getXpathElement(xpath).getText();
			
			endTimes = sdf.format(new Date().getTime());
			setXLValues("objects", 9, statusRow, "Pass");
			setXLValues("objects", 7, statusRow, actual1);
			setReports("objects", 12, reportStatus, "Text Pasted");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));
			}
			catch(Exception e){
				endTimes = sdf.format(new Date().getTime());
				setXLValues("objects", 9, statusRow, "Fail");
				setReports("objects", 12, reportStatus, "Text Not Pasted");
				setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));
				
			}

			break;
		
		case "dropdown":
			
			WebElement dropdown = getXpathElement(xpath);
			try{
			Select se = new Select(dropdown);
			se.selectByVisibleText(value);
			endTimes = sdf.format(new Date().getTime());

			setXLValues("objects", 9, statusRow, "Pass");
			setReports("objects", 12, reportStatus, "Dropdown works");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));


			}catch(Exception e){
			
			endTimes = sdf.format(new Date().getTime());
	
			setXLValues("objects", 9, statusRow, "Fail");
			setReports("objects", 12, reportStatus, "Dropdown not works");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

			}
			//se.selectByVisibleText(value);
			break;
			
		case "mouseover":
	
			try{
			Actions action = new Actions(driver);
			
			WebElement mousehover = getXpathElement(xpath);
			action.moveToElement(mousehover).perform();
			
			endTimes = sdf.format(new Date().getTime());

			setXLValues("objects", 9, statusRow, "Pass");
			setReports("objects", 12, reportStatus, "Mouse-hover works");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

			}catch (Exception e){

				endTimes = sdf.format(new Date().getTime());
				setXLValues("objects", 9, statusRow, "Fail");
				setReports("objects", 12, reportStatus, "Mouse-hover not works");
				setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

				
			}
			
			break;
	
		case "windowspopup":	
			
			break;
		
		case "frames":
			
			break;
			
		case "scrollelement":
           
			SpecialFunctions.scrollelementview(xpath);
            break;
            
		case "end":    
            SpecialFunctions.end(xpath);
            break;
			
		case "alertaccept":	
			
			Alert alert = driver.switchTo().alert();
			try{
			
			alert.accept();
			endTimes = sdf.format(new Date().getTime());

			setXLValues("objects", 9, statusRow, "Pass");	
			setReports("objects", 12, reportStatus, "Alert works");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));
			
			
			} catch (Exception e){
				
				endTimes = sdf.format(new Date().getTime());
				setXLValues("objects", 9, statusRow, "Fail");
				setReports("objects", 12, reportStatus, "Alert not works");
				setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));


			}
			
			break;
			
		case "alertdismiss":
			
			Alert alert1 = driver.switchTo().alert();
			try{
			alert1.dismiss();
			endTimes = sdf.format(new Date().getTime());

			setXLValues("objects", 9, statusRow, "Pass");
			setReports("objects", 12, reportStatus, "Alert dismissed");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

			}catch(Exception e){
				
				
				endTimes = sdf.format(new Date().getTime());
				setXLValues("objects", 9, statusRow, "Fail");
				setReports("objects", 12, reportStatus, "Alert not works");
				setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));


				
			}
			break;
			
		case "alertgettext":
			
			
			break;
			
		case "alertsendkeys":
			
			Alert alert2 = driver.switchTo().alert();
			try{
			driver.switchTo().alert().sendKeys(value);
			alert2.accept();
			endTimes = sdf.format(new Date().getTime());

			setXLValues("objects", 9, statusRow, "Pass");
			setReports("objects", 12, reportStatus, "Alert sendkeys works");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

			} catch (Exception e){
			
				endTimes = sdf.format(new Date().getTime());

				setXLValues("objects", 9, statusRow, "Fail");
				setReports("objects", 12, reportStatus, "Alert sendkeys not works");
				setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));
				
				
			}
			
			break;
			
		case "getsize":
			
			Dimension dimensionSize = driver.findElement(By.xpath(xpath)).getSize();
			
			int dimensionWidth = dimensionSize.width;
			int dimensionHeight = dimensionSize.height;
			
			try{
			
			endTimes = sdf.format(new Date().getTime());
			
				
			setXLValues("objects", 9, statusRow, "Pass");
			setXLValues("objects", 13, reportStatus, "(" +String.valueOf(dimensionWidth)+" , "+ String.valueOf(dimensionHeight)+ ")");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));
			setReports("objects", 12, reportStatus, "Size works fine");
			
			
			
			System.out.println("Dimension width is "+dimensionWidth);
			System.out.println("Dimension height is "+dimensionHeight);
			} catch(Exception e){
				
				endTimes = sdf.format(new Date().getTime());

				setXLValues("objects", 9, statusRow, "Fail");
				setXLValues("objects", 13, reportStatus, String.valueOf(dimensionWidth)+" , "+ String.valueOf(dimensionHeight));
				setReports("objects", 12, reportStatus, "Size doesn't work");
				setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));


				
			}
			
			break;
			
		case "getlocation":
			
			Point point = driver.findElement(By.xpath(xpath)).getLocation();
			int xLocation = point.x;
			int yLocation = point.y;
			try{
				
			endTimes = sdf.format(new Date().getTime());	
			
			setXLValues("objects", 9, statusRow, "Pass");
			setXLValues("objects", 13, reportStatus, "(" +String.valueOf(xLocation)+" , "+ String.valueOf(yLocation)+ ")");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));
			setReports("objects", 12, reportStatus, "Location works fine");
			
			} catch(Exception e){

				endTimes = sdf.format(new Date().getTime());

				setXLValues("objects", 9, statusRow, "Fail");
				setXLValues("objects", 13, reportStatus, String.valueOf(xLocation)+" , "+ String.valueOf(yLocation));
				setReports("objects", 12, reportStatus, "Location doesn't work");
				setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));	
				
			}
			break;
			
		case "uploadFile":	
			
			break;
			
		case "toolTip":
			
			break;
			
		case "datePicker":
			
			break;
			
		case "navigate":
			
			driver.navigate().to(value);
			
			break;
			
		case "forward":
			
			System.out.println("started");
			driver.navigate().forward();
			System.out.println("F completed");
			break;
			
		case "back":
			
			driver.navigate().back();
			
			break;
			
		case "refresh":
			System.out.println("started");

			driver.navigate().refresh();
			
			break;
			
		case "checkbox":
			
			break;
			
		case "WaitTillPageLoads":
			
            wait.until(new Function<WebDriver, Boolean>() {
                public Boolean apply(WebDriver driver) {
                return String
                .valueOf(((JavascriptExecutor) driver).executeScript("return document.readyState"))
                .equals("complete");
                }
                });
            break;
			
		case "Wait":
			//WebDriverWait wait = new WebDriverWait(driver, 6);
			try{
			WebElement ExpWait = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(xpath)));
			//Thread.sleep(9000);
			
			
			endTimes = sdf.format(new Date().getTime());

			setXLValues("objects", 9, statusRow, "Pass");
			setReports("objects", 12, reportStatus, "Wait works");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));


			}catch(Exception e){
			
			endTimes = sdf.format(new Date().getTime());
	
			setXLValues("objects", 9, statusRow, "Fail");
			setReports("objects", 12, reportStatus, "Wait not works");
			setXLValues("objects", 11, reportStatus, getCurrentTime(startTimes, endTimes));

			}
			
			break;	
		case "selectalloption":
			
			break;

        case "gettitle":
			
			String title = driver.getTitle();
			try{
			
			setXLValues("objects", 7, statusRow, title);
			}catch(Exception e){
				
				setXLValues("objects", 9, statusRow, "Fail");
				
			}
				break;
				
               
        case "getcurrenturl":		
			
        	String url = driver.getCurrentUrl();
        	try{
        		
        		setXLValues("objects", 7, statusRow, url);
        		
        	}catch(Exception e){
        		
        		setXLValues("objects", 9, statusRow, "Fail");
        		
        	}
        	
        	break;
        	
        case "RightArrow":  
        	
            SpecialFunctions.rightArrow(xpath, value);    
           try{
        		
        		setXLValues("objects", 7, statusRow, "Pass");
        		
        	}catch(Exception e){
        		
        		setXLValues("objects", 9, statusRow, "Fail");
        		
        	}
            break;
        	
        	
			
		}
		
		
		}catch(Exception e){
			setXLValues("objects", 9, statusRow, "Element not Found");			
				
			}
		
	}
	

	
}