class Block
{
    private readonly int _width;
    private readonly int _length;
    private readonly int _height;

    public Block(int[] dimensions) => (_width, _length, _height) = (dimensions[0], dimensions[1], dimensions[2]);

    public int GetWidth() => _width;
    public int GetLength() => _length;
    public int GetHeight() => _height;

    public int GetVolume() => _width * _length * _height;
    public int GetSurfaceArea() => 2 * (_width * _length + _length * _height + _height * _width);
}