package webScraper;

import org.jsoup.*;
import org.jsoup.examples.*;

public class webScraper {
	//Program will scrape a web page for raw html
	//Program will scrape metadata of photos, videos, and other media
	//Program will store URL data and have the ability to collect and display data
	//Program will take URL, strings to target, and strings to omit
	//Program will have the ability to store data found as well as setup data of strings to target and strings to omit
	
	public static void main(String[] args)
	{
		String content;
		try {
			content = URLConnectionReader.getText("https://en.wikipedia.org/wiki/\"Hello,_World!\"_program");
			content=new org.jsoup.examples.W3CDom.asString(Jsoup.parse(content));
			System.out.print(content);	
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		

	}
}
