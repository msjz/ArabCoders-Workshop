def atm(request):
    balance = 500
    if request <= balance:
        if request > 0:
            while request >= 100:
                print "give 100"
                request = request - 100
            while request >=50:
                print "give 50"
                request = request - 50
            while request >= 10:
                print "give 10"
                request = request - 10
            while request >= 5:
                print "give 5"
                request = request - 5
        if request< 5 and request > 0:
            print "give"+" "+str(request)
    if request > balance:
        print "out of balance"

atm(13)
