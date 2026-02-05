emails = ["user@gmail.com", "teste@", "admin@yahoo.com", "invalid", "email@site.com"]

emails = list(
    filter(lambda a: "@" in a and "." in a, emails)
)

print(emails)