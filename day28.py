#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    list_users = []
    final_user_list = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        fname_email = {}

        firstName = firstNameEmailID[0]
        
        emailID = firstNameEmailID[1]
        
        fname_email["firstName"] = firstName
        fname_email["email"] = emailID

        list_users.append(fname_email)

    for i, user in enumerate(list_users):
        if user['email'].split('@')[1].split('.')[0] != 'gmail':
            pass
        else:
            final_user_list.append(user)

    print("\n".join(sorted([x['firstName'] for x in final_user_list])))