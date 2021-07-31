# https://www.youtube.com/watch?v=uwrc4H3yaJ4&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=11

def process(n,source, destination, helper):
    if n == 0:
        return
    process(n-1,source, helper,destination,)
    print(n,source,destination,sep="",end='\n')
    process(n-1,helper,destination,source)


if __name__ == "__main__":
    process(5,"A",'B','C')