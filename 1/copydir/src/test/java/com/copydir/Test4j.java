package com.copydir;
import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Test4j {
    public static final Logger LOGGER = LoggerFactory.getLogger(Test4j.class);
 
    @Test
    public void test01(){
        //日志输出
        LOGGER.error("error");
        LOGGER.warn("wring");
        LOGGER.info("info");
        LOGGER.debug("debug");
        LOGGER.trace("trance");
 
        //占位符输出
        String name = "bysen";
        Integer age = 24;
        LOGGER.info("姓名{}，年龄{}",name,age);
 
        //异常处理
        // try{
        //     int i =1/0;
        // }catch (Exception e){
        //     LOGGER.error("发生异常：",e);
        // }
    }
}


 