import java.util.HashMap;
import java.util.Map;

public class Cache {

    private Map<String, Double> cache;

    public Cache() {
        this.cache = new HashMap<String, Double>();
    }

    private String Key(double base, double power) {
        // The key could be generated in a better fashion, e.g. as a hash
        return Double.toString(base) + "^" + Double.toString(power);
    }

    public boolean HasKey(double base, double power) {
        String key = Key(base, power);
        if(cache.get(key) != null) {
            return true;
        }
        else {
            return false;
        }
    }

    public void AddValue(double base, double power, double value) {
        String key = Key(base, power);
        cache.put(key, value);
    }

    public double GetValue(double base, double power) {
        String key = Key(base, power);
        return cache.get(key);
    }

}