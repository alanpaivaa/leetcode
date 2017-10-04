//Runs in linear time with constant space
bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {

    //now n can only be 1 or higher
    if(n==0){
        return 1;
    }

    //now flowerbedSize can only be 2 or higher
    if ((flowerbedSize==1) && n==1){
        return (flowerbed[0]==0);
    }
    int i = 0;
    int available_places = 0;

    while(n > 0 && i < flowerbedSize){
        if (i == 0){
            if(flowerbed[i] == 0 && flowerbed[i+1]==0){
                available_places++;
                i++;
            }
        }else{
            if(i == flowerbedSize - 1){
                if(flowerbed[flowerbedSize-1]==0 && flowerbed[flowerbedSize-2]==0){
                   available_places++;
                    i++;
                }
            }else{
                if(flowerbed[i - 1]==0 && flowerbed[i]==0 && flowerbed[i+1]==0){
                    available_places++;
                    i++;
                }
            }
        }
        i++;
    }

    return available_places>=n;
}
