package fr.aspanier.adventofcode2022.jour3;

import lombok.experimental.UtilityClass;

import java.util.HashMap;
import java.util.Map;

@UtilityClass
public class Jour3Utils {

    Map<Character, Integer> getPriorities() {
        char increment = 'a';
        Map<Character, Integer> priorities = new HashMap<>();

        for (int i = 1; i < 27; i++) {
            priorities.put(increment, i);
            increment++;
        }

        increment = 'A';
        for (int i = 27; i < 53; i++) {
            priorities.put(increment, i);
            increment++;
        }
        return priorities;
    }
}
