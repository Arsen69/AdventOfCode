package fr.aspanier.adventofcode2022.jour3;

import lombok.Getter;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

@Component
@Getter
@Setter
@Slf4j
public class Enigme2J3 {

    String path = "src\\main\\resources\\Jour3\\InputPuzzle1";

    public Integer exec() throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(path));

        Map<Character, Integer> priorities = Jour3Utils.getPriorities();

        Integer sum = 0;

        for (int i = 1; i <= lines.size(); i++) {

            if (i % 3 == 0) {
                HashSet<Character> sac1 =
                        (HashSet<Character>) lines.get(i - 1).chars().mapToObj(c -> (char) c).collect(Collectors.toSet());
                HashSet<Character> sac2 =
                        (HashSet<Character>) lines.get(i - 2).chars().mapToObj(c -> (char) c).collect(Collectors.toSet());
                HashSet<Character> sac3 =
                        (HashSet<Character>) lines.get(i - 3).chars().mapToObj(c -> (char) c).collect(Collectors.toSet());

                Character result = common(sac1, sac2, sac3);
                sum += priorities.get(result);
            }

        }

        log.info("La somme de toutes les priorités pour chaque groupe de 3 elfes est {}", sum);

        return sum;

    }

    static Character common(HashSet<Character> sac1, HashSet<Character> sac2, HashSet<Character> sac3) {

        // Creating empty hash table;
        HashMap<Character,
                Integer> hash = new HashMap<>();

        for (Character a : sac1) {
            hash.put(a, 1);
        }

        for (Character b : sac2) {

            // if the element is already exist in the
            // linked list set its frequency 2
            if (hash.containsKey(b))
                hash.put(b, 2);

        }

        for (Character c : sac3) {
            if (hash.containsKey(c) &&
                    hash.get(c) == 2)

                // if the element frequency is 2 it means
                // its present in both the first and second
                // linked list set its frequency 3
                hash.put(c, 3);

        }

        for (Map.Entry<Character,
                Integer> x : hash.entrySet()) {

            // if current frequency is 3 its means
            // element is common in all the given
            // linked list
            if (x.getValue() == 3)
                return x.getKey();
        }
        return null;
    }


}
