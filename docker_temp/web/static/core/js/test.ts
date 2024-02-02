const a = 1

const b = (a: number, b: string) => {
    console.log(this)
    return a + b
}
