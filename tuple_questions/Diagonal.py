'''
Diagonal

Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

Example

    input_tuple = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
    output_tuple = get_diagonal(input_tuple)
    print(output_tuple)  # Expected output: (1, 5, 9)
'''


def get_diagonal(tup):
    # TODO
    resut=tuple()
    for i in range(tup.__len__()):
         resut+=(tup[i][i],)
    return resut

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)

