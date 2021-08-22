package com.sl;
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class ServletDemo extends HttpServlet{
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.getRequestDispatcher("./hello.jsp").forward(request,response);
        // response.getWriter().append("Hello Hooyes!");
    }
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request,response);
    }
}
