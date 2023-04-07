public class ExternalClass {
    private int prNum;
    public int puNum;
    public ExternalClass() {
        puNum = 2;
        prNum = 1;
    }
    public String[] returnPuStringArray() {
        String[] result = {"1","2","3","4","5"};
        return result;
    }
    private String[] returnPrStringArray() {
        String[] result = {"1","2"};
        return result;
    }
}