package fr.aspanier.adventofcode2022.jour4;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.IOException;

import static org.assertj.core.api.Assertions.assertThat;

class J4Part1Test {

    static J4Part1 target;

    @BeforeAll
    static void init() {
        target = new J4Part1();
    }

    @Test
    @DisplayName("Doit renvoyer 2, le nombre de paires dans lesquels l'un contient complètement l'autre")
    void execTest() throws IOException {

        target.setPath("src\\test\\java\\fr\\aspanier\\adventofcode2022\\jour4\\J4Part1Test.java");

        Integer result = target.exec();

        assertThat(result).isEqualTo(2);
    }

}