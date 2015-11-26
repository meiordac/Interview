#include "stdio.h"
#include "stdlib.h"
#include "string.h"


typedef struct List{

	int value;
	struct List *next;
	struct List *previous;

} List;

const int CAPACITY = 1000;

int * AddToArray(int *dArray, char *input){

	char command[16];
	int valueadd;
	sscanf(input,"%s %d",command,&valueadd);

	int i = 0;

	if(dArray[0]==0){
		dArray[0] = valueadd;
		printf("Value added to array\n");
	}
	else{
		while(dArray[i]!=0){
			i++;
		}
		dArray[i] = valueadd;
		printf("Value added to array\n");
	}
	return dArray;
}

void PrintArray(int *dArray){

	int i = 0;
	while(dArray[i]!=0){
		printf("Position: %d Value: %d\n",i+1,dArray[i]);
		i++;
	}
	if(dArray[0]==0){
		printf("Array is empty\n");
	}
}

int * AddToArrayAt(int *dArray, char *input){

	char command[16];
	char command2[16];
	int valuetoins;
	int position;


	sscanf(input,"%s %s %d %d",command,command2,&valuetoins,&position);

	position = position-1;
	int posaux = position;
	int finalposition = 0;

	if(dArray[position]!=0){

		while(dArray[posaux]!=0){
			posaux++;
	}

	for(posaux; posaux>=position; posaux--){
		dArray[posaux+1] = dArray[posaux];
	}

	dArray[position] = valuetoins;
	printf("Value added\n");
	
	}

	return dArray;
}

int * DelNumArray(int *dArray, char *input){

	char command[16];
	int valuedel;
	int i=0;
	int posElementDelete = 0;

	sscanf(input,"%s %d",command,&valuedel);

	while(dArray[i]!=0){
		if(dArray[i]==valuedel){
			posElementDelete = i;
			break;
		}
		else{
			i++;
		}
	}

	if(posElementDelete==0){
		if(dArray[posElementDelete+1]==0){
			dArray[posElementDelete] = 0;
		}
		else if (dArray[posElementDelete+1]!=0){
			int j = 1;
			while(dArray[j]!=0){
				dArray[j-1] = dArray[j];
				j++;
			}
			dArray[j-1]=0;
		}
	}

	else if(dArray[posElementDelete+1]==0){
		dArray[posElementDelete] = 0;
	}

	else{
		int k = posElementDelete;
		while(dArray[k]!=0){
			dArray[k] = dArray[k+1];
			k++;
		}
		dArray[k-1]=0;
	}


	printf("Element deleted\n");
	

	return dArray;
}

int * DelNumArrayAt(int *dArray, char *input){

	char command[16];
	char command2[16];
	int position;

	sscanf(input,"%s %s %d",command, command2, &position);

	position = position-1;

	if(position==0){
		if(dArray[position+1]==0){
			dArray[position] = 0;
		}
		else if(dArray[position+1]!=0){
			int j = 1;
			while(dArray[j]!=0){
				dArray[j-1] = dArray[j];
				j++;
			}
			dArray[j-1]=0;
		}
	}
	else if (dArray[position+1]==0){
		dArray[position]=0;
	}
	else{
		int k = position;
		while(dArray[k]!=0){
			dArray[k] = dArray[k+1];
			k++;
		}
		dArray[k-1]=0;
	}			

	return dArray;

}

int * GetAtArray(int *dArray, char *input){

	char command[16];
	int position;

	sscanf(input,"%s %d",command, &position);

	printf("Number at position %d is: %d\n",position,dArray[position-1]);

	return dArray;

}

int *FindNumAtArray(int *dArray, char *input){

	char command[16];
	int numlooked;
	sscanf(input,"%s %d",command,&numlooked);
	
	int i;
	while (dArray[i]!=0){
		if(dArray[i]==numlooked){
			printf("Number found at index: %d\n",i+1);
			break;
		}
		else{
			i++;
		}
	}

	return dArray;

}

int *GetNumElementsArray(int *dArray){

	int i=0; 
	while (dArray[i]!=0){
		i++;
	}
	printf("Number of elements of Array: %d\n",i);

	return dArray;
}

int * ListToArray(List *start, int *dArray){

	List *currentList = start;

	int i = 0;
	while(dArray[i]!=0){
		dArray[i]=0;
		i++;
	}
	i = 0;

	if(currentList==NULL){
		dArray[0]=0;
	}
	else if(currentList->next==NULL){
		dArray[0]=currentList->value;
	}
	else{
		while(currentList->next!=NULL){
			dArray[i] = currentList->value;
			i++;
			currentList = currentList->next;
		}
		dArray[i] = currentList->value;
	}

	return dArray;

}

int *InvertArray(int *dArray){

	int *invArraypoint;
	int invArray[CAPACITY];
	invArraypoint = invArray;
	int lastposition = 0;

	while(dArray[lastposition]!=0){
		lastposition++;
	}
	lastposition--;

	printf("Last position is: %d",lastposition);

	int i;

	for(i=0; i<=lastposition; i++){
		invArraypoint[i] = dArray[lastposition-i];
	}

	return invArraypoint;

}

List *ArrayToList(List *start, int *dArray){

		List *current = start;
		
		int i = 0;

		while(dArray[i]!=0){
			List *newList = malloc(sizeof(List));
			newList->value = dArray[i];

			if(i==0){
				start = newList;
				current = start;
				current->next = NULL;
			}
			else{
				current->next = newList;
				newList->previous = current;
			}
			if(current->next!=NULL){
				current = current->next;
			}

			i++;
			printf("El valor del nodo Current es %d\n",current->value);
		}
		
		return start;
}

List *AddAt(List *start, char *input){

	char command[16];
	char command2[16];
	int valuetoins;
	int position;
	int posaux = 1;
	List *newNumber = malloc(sizeof(List));

	sscanf(input,"%s %s %d %d",command,command2,&valuetoins,&position);

	newNumber->value = valuetoins;

	List *currentList = start;
	List *numToDisplace = NULL;

	while (currentList!=NULL){
		if(position==posaux){
			numToDisplace = currentList;
			break;
		}
		posaux = posaux+1;
		currentList = currentList->next;
	}

	if(position==1){
	newNumber->next = start;
	start = newNumber;
	}

	else if(numToDisplace->next==NULL){
		newNumber->previous = numToDisplace->previous;
		newNumber->next = numToDisplace;
		numToDisplace->previous->next = newNumber;
		numToDisplace = newNumber;
	}

	else{
		newNumber->next = numToDisplace;
		newNumber->previous = numToDisplace->previous;
		numToDisplace->previous->next = newNumber;
		numToDisplace->previous = newNumber;
		numToDisplace = newNumber;

	}

	return start;
}

List *AddInteger(List *start, char *input){

	char command[16];
	int valueadd;
	sscanf(input,"%s %d",command,&valueadd);

	List *current = start;
	List *newList = malloc(sizeof(List));
	newList->value=valueadd;

	if (current==NULL){
		current = newList;
		current->next=NULL;
		printf("Added value to list: %d\n",valueadd);
		return current;
	}

	while(current->next!=NULL){
		current = current->next;
	}
	
	current->next = newList;
	newList->previous = current;

	printf("Added value to list: %d\n",valueadd);

	return start;

}

List *DelInteger(List *start, char *input){


	char command[16];
	int valuedel;

	sscanf(input,"%s %d",command,&valuedel);

	List *currentList = start;
	List *numToDelete = NULL;
	
	while (currentList!=NULL){
		if(currentList->value==valuedel){
			numToDelete = currentList;
			break;
		}

		currentList = currentList->next;
	}

	if(start!=NULL && numToDelete==start){
		if(numToDelete->next!=NULL){
			numToDelete->next->previous = NULL;
			start = numToDelete->next;
		}
		else{
			start = NULL;
		}
	}

	else if(start!=NULL && numToDelete!=start){
		if(numToDelete->next==NULL){
			numToDelete->previous->next=NULL;
		}
		else{
			numToDelete->next->previous = numToDelete->previous;
			numToDelete->previous->next = numToDelete->next;
		}

	}

	return start;

}

List *DelIntegerAt(List *start, char *input){

	char command[16];
	char command2[16];
	int posdelete;
	int posaux = 1;

	sscanf(input,"%s %s %d",command,command2, &posdelete);

	List *currentList = start;
	List *numToDelete = NULL;

	while (currentList!=NULL){
		if(posdelete==posaux){
			numToDelete = currentList;
			break;
		}
		posaux = posaux+1;
		currentList = currentList->next;
	}

	if(numToDelete==start){
		numToDelete->next->previous = NULL;
		start = numToDelete->next;
	}

	else if(numToDelete->next==NULL){
		numToDelete->previous->next=NULL;
	}
	else{
		numToDelete->previous->next = numToDelete->next;
		numToDelete->next->previous = numToDelete->previous;
	}

	return start;

}

List *Invert(List *start){

	List *returnPtr = start;

	List *temp = NULL;
	List *current = start;

	while (current!=NULL){
		temp = current->previous;
		current->previous = current->next;
		current->next = temp;
		current = current->previous;
	}

	if(temp!=NULL){
		start = temp->previous;
	}

	return start;

}

List *PrintList(List *start){

	List *currentList = start;
	int count = 0;

	while (currentList!=NULL){
		count++;
		printf("Position:%d Value:%d\n",count,currentList->value);
		currentList = currentList->next;
	}
	return start;

}

List *PrintQuanNumbers(List *start){

	List *currentList = start;
	int qnumbers = 0;

	if(start==NULL){
		qnumbers = 0;
	}
	else{
		while(currentList->next!=NULL){
			qnumbers++;
			currentList = currentList->next;
		}
		qnumbers++;
	}

	printf("Quantity of numbers: %d\n",qnumbers);

	return start;

}

List *GetAtPosition(List *start, char *input){

	char command[16];
	int position;
	sscanf(input,"%s %d",command,&position);
	int posaux = 1;

	List * currentList = start;
	List * numberLooked;

	while (currentList!=NULL){
		if(position==posaux){
			numberLooked = currentList;
			break;
		}
		posaux = posaux+1;
		currentList = currentList->next;
	}

	printf("Number is %d\n",numberLooked->value);

	return start;

}

List *FindNumber(List *start, char *input){

	char command[16];
	int numlooked;
	sscanf(input,"%s %d",command,&numlooked);
	int actualpos = 1;
	int posfound = 0;

	List * currentNum = start;

	while (currentNum->next!=NULL){
		if(currentNum->value==numlooked){
			posfound = actualpos;
			break;
		}
		else{
			currentNum = currentNum->next;
			actualpos = actualpos+1;
		}
	}

	if(currentNum->next==NULL && currentNum->value==numlooked && posfound==0){
		posfound = actualpos;
	}

	printf("Number found at position: %d\n",posfound);

	return start;

}


int main(){

	char command[16];
	char command2[16];
	char command3[16];
	char input[16];
	char structure[16];

	int *dArray;
	int numberList[CAPACITY];
	dArray = numberList;


	int valinput;
	int posinput;

	List *start = NULL;
	List *newest = NULL;

	while (fgets(input,15,stdin)){

		sscanf(input,"%s",command);


		if(strncmp(input,"SET LISTA",9)==0){
				strcpy(structure,"list");
				break;
			}
		else if (strncmp(input,"SET ARRAY",9)==0){
				strcpy(structure,"array");
				break;
			}
		else if(strncmp(input,"quit",4)==0){
			printf("Quitting\n\n");
			break;
		}	
		}

		if(strncmp(input,"quit",4)==0){
			printf("Quitting\n\n");
		}

	while (fgets(input,15,stdin)){

		sscanf(input,"%s %s",command,command2);

		if(strncmp(command,"ADD",3)==0 && strncmp(command2,"AT",2)!=0){
			if(strncmp(structure,"list",4)==0){
				start = AddInteger(start,input);
			}
			else{
				dArray = AddToArray(dArray,input);
			}
		}

		else if(strncmp(input,"ADD AT",6)==0){
			if(strncmp(structure,"list",4)==0){
				start = AddAt(start,input);
			}
			else{
				dArray = AddToArrayAt(dArray,input);
			}	
		}
		else if(strncmp(input,"DEL",3)==0 && strncmp(command2,"AT",2)!=0){
			if(strncmp(structure,"list",4)==0){
				start = DelInteger(start,input);
			}
			else{
				dArray = DelNumArray(dArray,input);
			}
		}
		else if(strncmp(input,"DEL AT",6)==0){
			if(strncmp(structure,"list",4)==0){
				start = DelIntegerAt(start,input);
			}
			else{
				dArray = DelNumArrayAt(dArray,input);
			}
		}
		else if(strncmp(input,"INV",3)==0){
			if(strncmp(structure,"list",4)==0){
				start = Invert(start);
			}
			else{
				dArray = InvertArray(dArray);
			}
		}
		else if(strncmp(input,"GET",3)==0){
			if(strncmp(structure,"list",4)==0){
				start = GetAtPosition(start,input);
			}
			else{
				dArray = GetAtArray(dArray,input);
			}
		}
		else if(strncmp(input,"FND",3)==0){
			if(strncmp(structure,"list",4)==0){
				start = FindNumber(start,input);
			}
			else{
				dArray = FindNumAtArray(dArray,input);
			}
		}
		else if(strncmp(input,"NUM",3)==0){
			if(strncmp(structure,"list",4)==0){
				start = PrintQuanNumbers(start);
			}
			else{
				dArray = GetNumElementsArray(dArray);
			}
		}
		else if(strncmp(command,"PRT",3)==0){
			if(strncmp(structure,"list",4)==0){
				start = PrintList(start);
			}
			else{
				PrintArray(dArray);
			}
		}
		else if(strncmp(input,"SET ARRAY",9)==0){
			dArray = ListToArray(start, dArray);
			strcpy(structure,"array");
		}
		else if(strncmp(input,"SET LISTA",9)==0){
			start = ArrayToList(start, dArray);
			strcpy(structure,"list");
		}
		else if(strncmp(input,"quit",4)==0){
			printf("Quitting\n\n");
			break;
		}
	}

	return 0;
}