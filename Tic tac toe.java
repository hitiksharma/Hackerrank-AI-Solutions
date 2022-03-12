import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

/* Complete the function below to print 2 integers separated by a single space which will be your next move */
    static void nextMove(String player, String [] board){
        char Empty ='_';
        int r=0;
        int c=0;
        char tmarker;
        char win =player.charAt(0);
        
        if(player.charAt(0)=='X'){
            tmarker='O';
        }else{
            tmarker='X';
        }
        // Check for empty board, if empty execute winning strat
        
        if (EmptyBoard(board)==true){
           
            if(board[1].charAt(1)==Empty){
                System.out.println("1 1");
                return;}
            // Look for win
            }else if(SearchBoard(player.charAt(0),board)){return;
            // Look for counter                             
            }else if(SearchBoard(tmarker,board)){return;
            //Make winning approach
            }else{
            
            
                //Make Play
                   if(board[1].charAt(1)==Empty){System.out.println("1 1");return;}
                   else if(board[0].charAt(0)==Empty){System.out.println("0 0");return;}
                   else if(board[0].charAt(2)==Empty){System.out.println("0 2");return;}
                   else if(board[2].charAt(0)==Empty){System.out.println("2 0");return;}
                   else if(board[2].charAt(2)==Empty){System.out.println("2 2");return;}
            
            
            
            
            
            
            
                
            }
            
            
            
            
        }
       
    
    
  private static boolean EmptyBoard(String[]board){
      
      for(int i = 0; i <board.length;i++){
          for(int x= 0 ; x<board[i].length();x++){
              if(board[i].charAt(x)!='_'){
                  return false;
              }
          }
      }
      return true;
  }
    
  public static boolean  SearchBoard(char x , String[]board){
      
         char Empty ='-';
         char tmarker=x;
         if(board[1].charAt(1)==tmarker){
            //top
            if(board[0].charAt(1)==tmarker && board[2].charAt(1)==Empty){
                // place at bottom to counter
                System.out.println("2 1");
                return true;
             //left
            }else if(board[1].charAt(0)==tmarker && board[1].charAt(2)==Empty){
                System.out.println("1 2");
                return true;
             //right
            }else if(board[1].charAt(2)==tmarker && board[1].charAt(0)==Empty) {
                System.out.println("1 0");
                return true;
             //bottom
            }else if(board[2].charAt(1)==tmarker && board[0].charAt(1)==Empty ){
                System.out.println("0 1");
                return true;
            }
                
        //Corner 0 0
        } else if(board[0].charAt(0)==tmarker){
            
                if(board[0].charAt(1)==tmarker && board[0].charAt(2)==Empty){
                    System.out.println("0 2");
                    return true;
                }else if(board[1].charAt(0)==tmarker && board[2].charAt(0)==Empty){
                    System.out.println("2 0");
                    return true;
                }else if(board[1].charAt(1)==tmarker  && board[2].charAt(2)==Empty){
                    System.out.println("2 2"); 
                    return true;
                    
                // Middle Gaps
                // Top and botoom
                }else if(board[2].charAt(0)==tmarker && board[1].charAt(0)==Empty){
                    System.out.println("1 0");
                    return true;
                 // Right//
                }else if(board[0].charAt(2)==tmarker && board[0].charAt(1)==Empty){
                    System.out.println("0 1");
                    return true;
                 // Middle
                }else if(board[2].charAt(2)==tmarker && board[1].charAt(1)==Empty){
                    System.out.println("1 1");
                    return true;
                }
            
            
            
            
            
        //Corner 0,2
        } else if(board[0].charAt(2)==tmarker){
            
                if(board[0].charAt(1)==tmarker && board[0].charAt(0)==Empty){
                    System.out.println("0 0");
                    return true;
                }else if(board[1].charAt(2)==tmarker && board[2].charAt(2)==Empty){
                    System.out.println("2 2");
                    return true;
                }else if(board[1].charAt(1)==tmarker  && board[2].charAt(2)==Empty){
                    System.out.println("2 1");  
                    return true;
                    
                 // Middle Gaps
                // Top and botoom
                }else if(board[2].charAt(2)==tmarker && board[1].charAt(2)==Empty){
                    System.out.println("1 2");
                    return true;
                 // Left//
                }else if(board[0].charAt(0)==tmarker && board[0].charAt(1)==Empty){
                    System.out.println("0 1");
                    return true;
                 // Middle
                }else if(board[2].charAt(0)==tmarker && board[1].charAt(1)==Empty){
                    System.out.println("1 1");
                    return true;    
                    
                    
                    
                    
                }
        //Corner 2,0
        }   else if(board[2].charAt(0)==tmarker){
            
                if(board[2].charAt(1)==tmarker && board[2].charAt(2)==Empty){
                    System.out.println("2 2");
                    return true;
                }else if(board[1].charAt(0)==tmarker && board[0].charAt(0)==Empty){
                    System.out.println("0 0");
                    return true;
                }else if(board[1].charAt(1)==tmarker  && board[0].charAt(2)==Empty){
                    System.out.println("0 2");  
                    return true;
                    
                    
                    
                          
                 // Middle Gaps
                // Top and botoom
                }else if(board[0].charAt(0)==tmarker && board[1].charAt(0)==Empty){
                    System.out.println("1 0");
                    return true;
                 // Right//
                }else if(board[2].charAt(2)==tmarker && board[2].charAt(1)==Empty){
                    System.out.println("2 1");
                    return true;
                 // Middle
                }else if(board[0].charAt(2)==tmarker && board[1].charAt(1)==Empty){
                    System.out.println("1 1");
                    return true;    
                    
                }
            
            
        // Corner 2 ,2
        }else if(board[0].charAt(2)==tmarker){
            
                if(board[1].charAt(1)==tmarker && board[0].charAt(0)==Empty){
                    System.out.println("0 0");
                    return true;
                }else if(board[2].charAt(1)==tmarker && board[2].charAt(0)==Empty){
                    System.out.println("2 0");
                    return true;
                }else if(board[1].charAt(2)==tmarker  && board[2].charAt(2)==Empty){
                    System.out.println("0 2");  
                    return true;
                    
                    
                      
                 // Middle Gaps
                // Top and botoom
                }else if(board[0].charAt(2)==tmarker && board[1].charAt(2)==Empty){
                    System.out.println("1 2");
                    return true;
                 // Left//
                }else if(board[2].charAt(0)==tmarker && board[2].charAt(1)==Empty){
                    System.out.println("2 1");
                    return true;
                 // Middle
                }else if(board[0].charAt(0)==tmarker && board[1].charAt(1)==Empty){
                    System.out.println("1 1");
                    return true;    
                    
                }
 
        //Look for Win
        }
        return false;
      
      
  }
 
  
  public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String player;
        String board[] = new String[3];

        //If player is X, I'm the first player.
        //If player is O, I'm the second player.
        player = in.next();

        //Read the board now. The board is a 3x3 array filled with X, O or _.
        for(int i = 0; i < 3; i++) {
            board[i] = in.next();
        }

        nextMove(player,board);   
    
    }
}
