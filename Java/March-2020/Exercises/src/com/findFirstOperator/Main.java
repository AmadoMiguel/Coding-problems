package com.findFirstOperator;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Stack;

import com.findFirstOperator.model.Operator;

public class Main {

	public static void main(String[] args) {
		String[] arithmeticExpressions = {
				"(2 + 2) * 2",
				"2 + 2 * 2",
				"((2 + 2) * 2) * 3 + (2 + (2 * 2))",
				"2 + 3 * 45 * 56 + 198 + 10938 * 102938 + 5",
				"1022224552222222 * 3"
		};
		Arrays.asList(arithmeticExpressions).forEach((expr) -> {
			System.out.println(firstOperationCharacter(expr));
		});
	}
	
	private static int firstOperationCharacter(String expr) {
	    PriorityQueue<Operator> pq = new PriorityQueue<>(
		new Comparator<Operator>() {
	        @Override
	        public int compare(Operator o1, Operator o2) {
	            return Integer.compare(o1.getPriority(), o2.getPriority()) * (-1);
	        }
	    });
	    Stack<String> parenStack = new Stack<>();
	    int exprLenght = expr.length();
	    for (int i = 0; i < exprLenght; i++) {
	        char currChar = expr.charAt(i);
	        switch (currChar) {
	            case '(':
	                parenStack.add(String.valueOf(currChar));
	                break;
	            case ')':
	                parenStack.pop();
	                break;    
	            case '+':
	                if (!parenStack.empty()) {
	                    pq.add(new Operator(String.valueOf(currChar), i, 
	                    		5 + parenStack.size()));
	                } else {
	                    pq.add(new Operator(String.valueOf(currChar), i, 2));
	                }
	                break;
	            case '*':
	                if (!parenStack.empty()) {
	                    pq.add(new Operator(String.valueOf(currChar), i, 
	                    		7 + parenStack.size()));
	                } else {
	                    pq.add(new Operator(String.valueOf(currChar), i, 3));
	                }
	                break;
	        }
	    }
	    return pq.peek().getIndex();
	}

}
