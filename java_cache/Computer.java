
public class Computer {

    private Cache cache;

    public Computer() {
        this.cache = new Cache();
    }

    public double Compute(double base, double power) {
        double value;

        if(cache.HasKey(base, power)) {
            // Retrieve from cache
            value = cache.GetValue(base, power);
            System.out.println(String.format("Retrieving from cache: %.2f^%.2f = %.2f", base, power, value));
            return value;
        }

        // Store in cache
        value = Math.pow(base, power);
        cache.AddValue(base, power, value);
        System.out.println(String.format("Computing and storing in cache: %.2f^%.2f = %.2f", base, power, value));
        return value;
    }

}
