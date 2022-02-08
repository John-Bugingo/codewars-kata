// this is to help in getting abbrevirion of two words
function abbrevName(name) {
    name = name.toUpperCase().split(' ')
    return name[0][0] + "." + name[1][0]
}

console.log(abbrevName("joseph coder"));
