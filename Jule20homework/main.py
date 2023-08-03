def get_diag_words(array):
    if not array:
        return ""
    row = ''
    col = ''

    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                row+=array[i][j]
            if i+j == len(array)-1:
                col +=array[i][j]
    return row + ' ' + col
def test_get_diag_words():
    input = [['ж','ф','л'],
             ['р','и','а'],
             ['с','з','л']]
    expect = "жил лис"
    assert get_diag_words(input) == expect
    input = [['б', 'ф', 'л', 'т', ']', 'в'],
             ['р', 'е', 'а', 'о', 'о', 'щ'],
             ['е', 'и', 'л', 'р', 'э', 'к'],
             ['г', 'ы', 'о', 'а', 'ф', 'о'],
             ['н', 'н', 'а', 'а', 'я', 'ч'],
             ['а', 'з', 'л', 'ц', 'в', ' ']]
    expect = "белая  ворона"
    assert get_diag_words(input) == expect

    input = []
    expect = ""
    assert get_diag_words(input) == expect
test_get_diag_words()





def test_get_diag_words():
    input = [['ж','ф','л'],
             ['р','и','а'],
             ['с','з','л']]
    expect = "жил лис"
    assert get_diag_words(input) == expect

    input = [['б','ф','л','т',']','в'],
             ['р','е','а','о','о','щ'],
             ['е','и','л','р','э','к'],
             ['г','ы','о','а','ф','о'],
             ['н','н','а','а','я','ч'],
             ['а','з','л','ц','в',' ']]
    expect = "белая  ворона"
    assert get_diag_words(input) == expect

    input = []
    expect = ""
    assert get_diag_words(input) == expect

test_get_diag_words()
