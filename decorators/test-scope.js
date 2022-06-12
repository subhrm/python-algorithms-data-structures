function test_add(n) {
    function add(x,y){
        return x+y+n+m;
    }

    return add;
}

m = 10;
t2 = test_add(2);
console.log(t2(5,6));
t3 = test_add(3);
console.log(t3(5,6));