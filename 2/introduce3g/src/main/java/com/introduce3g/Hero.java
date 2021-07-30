package com.introduce3g;
import java.io.*;

public class Hero implements Hero_inter, Serializable{
    int id;
    String CNname, ENname, NikeName;
    int price;
    int [] value; 
    String Intro;
    Hero(String str, int id){
        String [] strs = str.split(" ");
        this.id = id;
        this.CNname = strs[0];
        this.ENname = strs[1];
        this.NikeName = strs[2];
        this.price = Integer.parseInt(strs[3]);
        this.value = new int[4];
        this.value[0] = Integer.parseInt(strs[4]);
        this.value[1] = Integer.parseInt(strs[5]);
        this.value[2] = Integer.parseInt(strs[6]);
        this.value[3] = Integer.parseInt(strs[7]);
        this.Intro = strs[8];
    }
    public boolean nameIs(String str){
        return this.CNname.equalsIgnoreCase(str) || 
               this.ENname.equalsIgnoreCase(str) ||
               this.NikeName.equalsIgnoreCase(str);
    }

    public boolean allIs(String str){
        return this.CNname.indexOf(str)!=-1 || 
               this.ENname.indexOf(str)!=-1 || 
               this.NikeName.indexOf(str)!=-1 ||
               this.Intro.indexOf(str)!=-1;
    }

    public static int findName(Hero [] heros, String str, int l, int r, Hero [] ans){
        int flag = 0;
        for(int i = l; i <= r; i++){
            if(heros[i].nameIs(str))
                ans[flag++] = heros[i];
        }
        return flag;
    }

    public static int findAll(Hero [] heros, String str, int l, int r, Hero [] ans){
        int flag = 0;
        for(int i = l; i <= r; i++){
            if(heros[i].allIs(str))
                ans[flag++] = heros[i];
        }
        return flag;
    }
    public void show(){
        System.out.printf("---------------------------------------\n");
        System.out.printf("名称：%s/%s\n称号：%s\n", this.CNname, this.ENname, this.NikeName);
        System.out.printf("价格：\033[1;33;40m%d\033[0m\n", this.price);
        System.out.printf("属性（物理/魔法/防御/难度）：\033[1;31;40m%d\033[0m/\033[1;34;40m%d\033[0m/\033[1;32;40m%d\033[0m/\033[1;35;40m%d\033[0m\n", 
        this.value[0], this.value[1], this.value[2], this.value[3]);
        System.out.printf("背景：%s\n", this.Intro);
        System.out.printf("---------------------------------------\n");
    }
    
}
/*

*/