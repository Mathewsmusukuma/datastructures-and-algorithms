def ratate_image(matrix):
    """"Do not return anythin in this function"""
    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # Save the top letf
            topLeft = matrix[top][left + i]
            # Move the botton left into top left
            matrix[top][left + i] = matrix[bottom - i][left]
            #  Move the bottom right in the bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # Move top right into the bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # Move top left into top right
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
    # If asked to return anything, then return a matrix by commenting out the code bellow
    #return matrix   
