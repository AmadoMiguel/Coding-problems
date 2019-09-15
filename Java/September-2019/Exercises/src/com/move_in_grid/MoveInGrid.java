package com.move_in_grid;

import java.util.ArrayList;
import java.util.List;

public class MoveInGrid {

	public static void main(String[] args) {
		List<List<Integer>> positionsInGrid = new ArrayList<List<Integer>>();
		List<Integer> pos1 = new ArrayList<Integer>();
		pos1.add(0);
		pos1.add(0);
		List<Integer> pos2 = new ArrayList<Integer>();
		pos2.add(1);
		pos2.add(3);
		List<Integer> pos3 = new ArrayList<Integer>();
		pos3.add(1);
		pos3.add(2);
		positionsInGrid.add(pos1);
		positionsInGrid.add(pos2);
		positionsInGrid.add(pos3);
		int nSteps = numberOfSteps(positionsInGrid);
		System.out.println(nSteps);
	}
	
	public static int numberOfSteps(List<List<Integer>> positions) {
		System.out.println(positions);
//		Iterate over each position and use an internal while loop to check if the 
//		next position was reached after certain number of steps
		int currentIndex = 0;
		int nSteps = 0;
		for (List<Integer> p : positions.subList(0, positions.size()-1)) {
			List<Integer> currentPosition = p;
			List<Integer> nextPosition = positions.get(currentIndex + 1);
			while((currentPosition.get(0) != nextPosition.get(0)) ||
				  (currentPosition.get(1) != nextPosition.get(1))) {
				System.out.println("Current: "+currentPosition);
				System.out.println("Next: "+nextPosition);
				System.out.println();
				currentPosition = moveOneStep(currentPosition, nextPosition);
				nSteps += 1;
			}
			currentIndex += 1;
		}
		return nSteps;
	}
	
	public static List<Integer> moveOneStep(List<Integer> currentPosition,
											List<Integer> nextPosition) {
//		Compare current position and next position to see how the next step is 
//		going to be like
		List<Integer> nextStep = new ArrayList<Integer>();
		if ((nextPosition.get(0) > currentPosition.get(0)) 
				&& (nextPosition.get(1) == currentPosition.get(1)) ) {
			nextStep.add(currentPosition.get(0) + 1);
			nextStep.add(currentPosition.get(1));
		} else if ((nextPosition.get(0) < currentPosition.get(0)) 
				&& (nextPosition.get(1) == currentPosition.get(1))) {
			nextStep.add(currentPosition.get(0) - 1);
			nextStep.add(currentPosition.get(1));
		} else if ((nextPosition.get(0) == currentPosition.get(0)) 
				&& (nextPosition.get(1) > currentPosition.get(1))) {
			nextStep.add(currentPosition.get(0));
			nextStep.add(currentPosition.get(1) + 1);
		} else if ((nextPosition.get(0) == currentPosition.get(0)) 
				&& (nextPosition.get(1) < currentPosition.get(1))) {
			nextStep.add(currentPosition.get(0));
			nextStep.add(currentPosition.get(1) - 1);
		} else if ((nextPosition.get(0) < currentPosition.get(0)) 
				&& (nextPosition.get(1) < currentPosition.get(1))) {
			nextPosition.add(currentPosition.get(0) - 1);
			nextPosition.add(currentPosition.get(1) - 1);
		} else if ((nextPosition.get(0) > currentPosition.get(0)) 
				&& (nextPosition.get(1) > currentPosition.get(1))) {
			nextStep.add(currentPosition.get(0) + 1);
			nextStep.add(currentPosition.get(1) + 1);
		} else if ((nextPosition.get(0) < currentPosition.get(0)) 
				&& (nextPosition.get(1) > currentPosition.get(1))) {
			nextStep.add(currentPosition.get(0) - 1);
			nextStep.add(currentPosition.get(1) + 1);
		} else if ((nextPosition.get(0) > currentPosition.get(0)) 
				&& (nextPosition.get(1) < currentPosition.get(1))) {
			nextStep.add(currentPosition.get(0) + 1);
			nextStep.add(currentPosition.get(1) - 1);
		} else {
			nextStep = currentPosition;
		}
		return nextStep;
	}

}
