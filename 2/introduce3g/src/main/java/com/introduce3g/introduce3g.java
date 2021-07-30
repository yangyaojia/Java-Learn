package com.introduce3g;

// import org.slf4j.Logger;
// import org.slf4j.LoggerFactory;
import java.io.*;
import lombok.extern.slf4j.Slf4j;

/**
 * Hello world!
 */

@Slf4j
public final class introduce3g {
    // public static final Logger LOGGER = LoggerFactory.getLogger(introduce3g.class);
    public static Hero [] heros = new Hero[100];
    public static int num = 0;
    static void AskName() throws Exception {
        System.out.printf("请输入英雄名称：\n");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine().strip();
        
        Hero [] ans = new Hero[num];
        int cnt = Hero.findName(heros, str, 1, num, ans);
        
        if(cnt == 0) {
            System.out.printf("没找到\n");
        }else{
            System.out.printf("找到 %d 个结果\n", cnt);
            for(int i = 0; i < cnt; i++) ans[i].show();
        }
    }

    static void ShowAll(){
        for(int i = 1; i <= num; i++){
            heros[i].show();
            System.out.println("");
        }
    }

    static void FindHero() throws Exception {
        System.out.printf("请输入关键字：\n");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine().strip();
        Hero [] ans = new Hero[num];
        int cnt = Hero.findAll(heros, str, 1, num, ans);
        
        if(cnt == 0) {
            System.out.printf("没找到\n");
        }else{
            System.out.printf("找到 %d 个结果\n", cnt);
            for(int i = 0; i < cnt; i++) ans[i].show();
        }
    }

    static int server() throws Exception {
        System.out.printf("---------------------------------------\n");
        System.out.printf("请选择一下功能：\n");
        System.out.printf("【1】 查询英雄名称\n");
        System.out.printf("【2】 显示所有英雄\n");
        System.out.printf("【3】 模糊（单关键字）查询英雄\n");
        System.out.printf("【0】 退出\n");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int choice = -1;
        while(true){
            System.out.printf("请输入编号：\n");
            String str = br.readLine();
            try{ choice = Integer.parseInt(str);}
            catch (NumberFormatException i) {
                System.out.printf("输入的不是数字！再来一次!\n");
                continue;
            }
            break;
        }
        if(choice == 0) return 0;
        else if(choice == 1) {AskName();return 1;}
        else if(choice == 2) {ShowAll();return 1;}
        else if(choice == 3) {FindHero();return 1;}
        else {System.out.println("听不懂你在说什么，再说一遍看？");return 1;}
    }
    public static void main(String[] args) throws Exception{

        log.info("Loading Data......");
        // LOGGER.info("Loading Data......");
        File data = new File("./data.txt");
        while(!data.exists()){
            System.out.printf("未找到数据文件，请从新指定文件位置与名称！:");
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String str = br.readLine().strip();
            data = new File(str);
        }
        FileReader fsr  = new FileReader(data);
        BufferedReader br = new BufferedReader(fsr);
        String str = br.readLine();
        

        while(str != null){
            heros[++num] = new Hero(str, num);
            str = br.readLine();
        }
        br.close();
        fsr.close();

        while(server()!=0);



    }
}


/*
艾希 Ashe 寒冰射手 450 7 2 3 4 作为阿瓦罗萨部族的战母
*/