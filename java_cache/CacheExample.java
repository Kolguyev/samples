
public class CacheExample {

    public static void main(String[] args) {
        double value;
        Computer computer = new Computer();

        // Compute first time (will be stored in cache)
        value = computer.Compute(5.0, 2.0);
        System.out.println(String.format("1) Computed value is %.2f.", value));

        // Compute second time (retrieve from cache)
        value = computer.Compute(5.0, 2.0);
        System.out.println(String.format("2) Computed value is %.2f.", value));

        // Compute some other value (will be stored in cache)
        value = computer.Compute(5.0, 3.0);
        System.out.println(String.format("3) Computed value is %.2f.", value));
    }
}