from demos import analyze_func,email_generator,bisection_iter

domain_list = ['example.com','gmail.com','yahoo.com']
email_count = 20
username_length = 12
email_list = analyze_func(email_generator,username_length,
    email_count,domain_list)
# print(email_list)

key_email = 'vds@example.com'

email_list.append(key_email)

email_list = analyze_func(sorted,email_list)

key_index, msg = analyze_func(bisection_iter, key_email, email_list)

print (msg)

if key_index:
    print(f"Value of index {key_index+1} is \
{email_list[key_index]}")
# if key_index < 0:
#     print(f"{key_email} is not present in the email list.")
# else:
#     print(f"{key_email} is present at \
#     {key_index+1} index in email list.")
#     print(f"Value of index {key_index+1} is \
#     {email_list[key_index]}")
