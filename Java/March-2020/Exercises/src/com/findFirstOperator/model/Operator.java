package com.findFirstOperator.model;

public class Operator {
	private String operator;
    private int index;
    private int priority;
    public Operator(String oper, int index, int p) {
        this.operator = oper;
        this.index = index;
        this.priority = p;
    }
    public String getOperator() {
        return this.operator;
    }
    public int getIndex() {
        return this.index;
    }
    public int getPriority() {
        return this.priority;
    }
}
