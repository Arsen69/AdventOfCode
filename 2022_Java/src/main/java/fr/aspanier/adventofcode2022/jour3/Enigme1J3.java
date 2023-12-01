package fr.aspanier.adventofcode2022.jour3;

import lombok.Getter;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import org.springframework.util.CollectionUtils;

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
public class Enigme1J3 {

    String path = "src\\main\\resources\\Jour3\\InputPuzzle1";

    public Integer exec() throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(path));


        Map<Character, Integer> priorities = Jour3Utils.getPriorities();

        Integer sum = 0;

        for (String line : lines) {

            HashSet<Character> compartiment1 =
                    (HashSet<Character>) line.substring(0, line.length() / 2).chars().mapToObj(c -> (char) c).collect(Collectors.toSet());
            HashSet<Character> compartiment2 =
                    (HashSet<Character>) line.substring(line.length() / 2).chars().mapToObj(c -> (char) c).collect(Collectors.toSet());

            Character result = CollectionUtils.findFirstMatch(compartiment1, compartiment2);

            sum += priorities.get(result);
        }

        log.info("La somme de toutes les priorités est {}", sum);

        return sum;

    }
}
