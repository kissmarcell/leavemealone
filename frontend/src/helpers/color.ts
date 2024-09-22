export const isLight = (color: string) => {
  if (color.length == 7) {
    const rgb = [
      parseInt(color.substring(1, 3), 16),
      parseInt(color.substring(3, 5), 16),
      parseInt(color.substring(5), 16),
    ];
    const luminance =
      (0.2126 * rgb[0]) / 255 +
      (0.7152 * rgb[1]) / 255 +
      (0.0722 * rgb[2]) / 255;
    return luminance > 0.5;
  }
  return false;
};
