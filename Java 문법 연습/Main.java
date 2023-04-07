import java.net.SocketPermission;

public class Main {
    public static void main(String[] args){
        final ExternalClass externalClass = new ExternalClass(); 
        //  externalClass = new ExternalClass(); // final로 선언했으므로 재할당 불가능
        String[] strArray = externalClass.returnPuStringArray();
        System.out.println("public int : " + externalClass.puNum);
        System.out.println("private int : " + externalClass.getprivateNum());
        System.out.print("배열 :");
        for(String s: strArray) {
            System.out.print(" " + s);
        }
        System.out.println();
    }
} 