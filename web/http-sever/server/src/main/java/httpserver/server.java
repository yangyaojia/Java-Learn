// package httpserver;

/**
 * Hello world!
 *
 */
import java.net.*;
import java.io.*;

public class server     
{
    public static void main( String[] args )
    {
        try{
            ServerSocket ss = new ServerSocket(8888);
            while(true){
                Socket socket = ss.accept();
                BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                String requestHeader;
                // while((requestHeader = br.readLine()) != null && !requestHeader.isEmpty()){
                //     System.out.println(requestHeader);
                // }
                File f = new File("./index.html");
                PrintWriter pw = new PrintWriter(socket.getOutputStream());
                String context;
                BufferedReader fr = new BufferedReader(new FileReader(f));
                pw.println("HTTP/1.1 200 OK");
                pw.println("Content-type:text/html");
                pw.println();
                while((context = fr.readLine()) != null){
                    pw.println(context);
                }
                // pw.println("<h1>Fuck</h1>");
                pw.flush();

                
                // OutputStream out = socket.getOutputStream();
                // out.write("HTTP/1.1 200 OK\r\n".getBytes());
                // out.write("Content-type:text/html\r\n".getBytes());
                // out.write("\r\n".getBytes());
                // out.write("<h1>Fuck哈哈</h1>\r\n".getBytes());
                
                br.close();
                // out.close();
                // pw.close();
            }

        }catch (IOException err){
            err.printStackTrace();
        }
    }
}
