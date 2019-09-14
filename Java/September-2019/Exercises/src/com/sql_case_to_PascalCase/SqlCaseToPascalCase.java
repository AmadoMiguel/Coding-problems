package com.sql_case_to_PascalCase;

public class SqlCaseToPascalCase {
	public static void main(String[] args) {
		String pascalCaseWord = sqlCaseToPascalCase("spring_is_awesome");
		System.out.println(pascalCaseWord);
	}
	public static String sqlCaseToPascalCase(String sqlString) {
//		Store each word of the sql string in an array
		String[] words = sqlString.split("_");
//		Iterate over each word, capitalize and join into the final string
		String convertedString = "";
//		Avoid unchecked exception(s)
		if (words.length > 0) {
			for (String w : words) {
				String firstCapitalLetter = w.substring(0,1).toUpperCase();
				convertedString += firstCapitalLetter + w.substring(1,w.length());
			}
			return convertedString;
		} else {
			return sqlString;
		}
	}
}
