package com.copydir;

import java.io.*;
import java.nio.channels.FileChannel;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CopyDir {

    public static final Logger LOGGER = LoggerFactory.getLogger(CopyDir.class);
    static void copyfile(File a, File b) throws IOException{
        FileInputStream fis = new FileInputStream(a);
        FileOutputStream fos = new FileOutputStream(b);

        FileChannel fci = fis.getChannel();
        FileChannel fco = fos.getChannel();

        // if(!b.exists()) b.createNewFile();
        // int c = 0;
        // while((c = fis.read())!=-1){
        //     fos.write((byte)c);
        // }
        fco.transferFrom(fci, 0, fci.size());
        LOGGER.info("Copy " + a.getPath() + " to " + b.getPath());
        fis.close();
        fos.close();
        fci.close();
        fco.close();
    } 
    static void copydir(File a, File b) throws IOException {
        if(a.isFile()){
            copyfile(a, b);
            return ;
        }
        LOGGER.info("Enter " + a.getPath());
        b.mkdirs();
        for(File s: a.listFiles()){
            copydir(s, new File(b.getPath() + "/" + s.getName()));
        }
    }
    static void err(String msg){
        LOGGER.error(msg);
    }
    public static void main(String[] args) throws IOException{
        
        if(args.length < 2) {err("Error args");return ;}
        File fa = new File(args[0]);
        File fb = new File(args[1]);
        if(!fa.isDirectory()) {err("Souces is not a Directory"); return ;}
        copydir(fa, fb);
        
    }
}

/*
//级别为debug的日志
logger.debug("Hello! debug!");
//级别为info的日志
logger.info("Hello! info!");
//级别为warn的日志
logger.warn("Hello! warn!");
//级别为error的日志
logger.error("Hello! error!");
*/