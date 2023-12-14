from ..ifelseif.ex3 import ex3

#test_ex3_positive_input
def test_ex3_positive_input():
    #Arrange
    x = 5
    
    #Act
    result = ex3(x)
    
    #Assert
    assert result == 15
    
#test_ex3_negative_input
def test_ex3_negative_input():
    #Arrange
    x = -5
    
    #Act
    result = ex3(x)
    
    #Assert
    assert result == -15
    
#test_ex3_zero_input
def test_ex3_zero_input():
    #Arrange
    x = 0
    
    #Act
    result = ex3(x)
    
    #Assert
    assert result == 0