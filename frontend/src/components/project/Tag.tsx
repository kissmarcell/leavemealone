import Colors from "@/constants/Colors";
import { isLight } from "@/helpers/color";
import stc from "string-to-color";

type TagProps = {
  name: string;
};

const Tag = (props: TagProps) => {
  const bgColor = stc(props.name);
  const fontColor = isLight(bgColor) ? Colors.black : Colors.white;

  return (
    <div
      style={{ ...styles.status, backgroundColor: bgColor, color: fontColor }}
    >
      {props.name}
    </div>
  );
};

const styles = {
  status: {
    fontSize: 15,
    padding: "5px 15px",
    borderRadius: 30,
  },
};

export default Tag;
