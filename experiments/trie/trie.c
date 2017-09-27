#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
#define LETTERS 27
#define ENTRY_LEN 21
//#define EOF '\0'
typedef struct node node;
struct node{
    _Bool entry;
    node* pChildren[LETTERS];
};

int initNode(node* root){
    root->entry = 0;
    for(int i=0; i<LETTERS; i++){
        root->pChildren[i] = NULL;
    }
}

int addNode(node* root, char* key){
    int pos = 0;
    if(key[pos] != EOF){
        if(root->pChildren[key[pos] - 'a'] != NULL){
            addNode(root->pChildren[key[pos] - 'a'], (key + ++pos));            
        }
        else{
            //No existing entry
            node nextNode;
            initNode(&nextNode);
            if(key[pos + 1] == EOF){
                nextNode.entry = 1;
            }
            root->pChildren[key[pos] - 'a'] = &nextNode;
            addNode(&nextNode, key[pos++]);
        }
    }
}

int sumEntries(node* root){
    /**
     * Return the total count of roots children that have
     * entry==True
     * **/
    
    int count = 0;
    else if(root->entry){
        count++;
        }
    
    for(int j=0; j<LETTERS; j++){
        if(root->pChildren[j] != NULL){
            count += sumEntries(root->pChildren[j]);
        }
    
    return count;

    }
int findNode(node* root, char* key){
    /**
     * Search through the tree w/ each letter of the key
     * When the key runs out return the sum of all nodes in the 
     * children that have entry == True
     * **/
    int pos = 0;
    int count = 0;
    if(key[pos] != EOF){//walk down the tree
        for(int j=0; j<LETTERS; j++){
            if(root->pChildren[j]->key[0] == key[pos]){
                findNode(root->pChildren[j], key[++pos]);
                break;
            }
        }
    }
    else{//Key is exhausted
        count += sumEntries(root);
    }
    return count;
}

/*
int main(){
    int n; 
    scanf("%d",&n);
    for(int a0 = 0; a0 < n; a0++){
        char* op = (char *)malloc(512000 * sizeof(char));
        char* contact = (char *)malloc(512000 * sizeof(char));
        scanf("%s %s",op,contact);
    }
    return 0;
}
*/
int main(void){
    node root;
    initNode(root);
    char[21] add = 'add';
    char[21] find = 'find';
    char[21] entry1 = 'hack';
    char[21] entry2 = 'hacker';
    char[21] testEntry = 'hac';
    
    addNode(root, entry1);
    addNode(root, entry2);
    printf("%d", findNode(root, testEntry));
}