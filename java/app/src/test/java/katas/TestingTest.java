package katas;

import java.util.Arrays;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestingTest {
    @Test
    public void basicTests() {
        assertEquals(Arrays.asList(), Testing.number(Arrays.asList()));
        assertEquals(Arrays.asList("1: a", "2: b", "3: c"), Testing.number(Arrays.asList("a", "b", "c")));
        assertEquals(Arrays.asList("1: ", "2: ", "3: ", "4: ", "5: "), Testing.number(Arrays.asList("", "", "", "", "")));
    }
}
