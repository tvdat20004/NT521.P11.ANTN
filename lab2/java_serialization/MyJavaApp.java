import java.io.*;
public class MyJavaApp{
    public static void main(String args[]) throws Exception{
        FileInputStream fis = new FileInputStream("normalObj.serial");
        ObjectInputStream ois = new ObjectInputStream(fis);
        NormalObj unserObj = (NormalObj)ois.readObject();
        ois.close();
    }
}
class NormalObj implements Serializable{
    public String name;
    public NormalObj(String name){
        this.name = name;
    }
    private void readObject(java.io.ObjectInputStream in) throws IOException,
    ClassNotFoundException{
        in.defaultReadObject();
        System.out.println(this.name);
    }
}
class VulnObj implements Serializable{
    public String cmd;
    public VulnObj(String cmd){
        this.cmd = cmd;
    }
    private void readObject(java.io.ObjectInputStream in) throws IOException,
    ClassNotFoundException{
        in.defaultReadObject();
        String s = null;
        Process p = Runtime.getRuntime().exec(this.cmd);
        BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
        while ((s = stdInput.readLine()) != null) {
            System.out.println(s);
        }
    }
}