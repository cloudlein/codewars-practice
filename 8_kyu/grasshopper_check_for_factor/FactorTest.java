import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class FactorTest {
    @Test
    public void basicTests() {
        // Test for factors (True)
        assertTrue(Kata.checkForFactor(10, 2));
        assertTrue(Kata.checkForFactor(63, 7));
        assertTrue(Kata.checkForFactor(2450, 5));
        assertTrue(Kata.checkForFactor(24612, 3));
        
        // Test for non-factors (False)
        assertFalse(Kata.checkForFactor(9, 2));
        assertFalse(Kata.checkForFactor(653, 7));
        assertFalse(Kata.checkForFactor(2453, 5));
        assertFalse(Kata.checkForFactor(24617, 3));
    }
}