import Colors from "@/constants/Colors";
import { isLight } from "@/helpers/color";
import stc from "string-to-color";

type TaskProps = {
    name: string;
    link: string;
    status?: string;
};

const Task = (props: TaskProps) => {
    const bgColor = stc(props.status);
    const fontColor = isLight(bgColor) ? Colors.black : Colors.white;

  return (
    <div style={styles.container}>
      <a href={props.link} target="_blank">{props.name}</a>
      { props.status && <div style={{...styles.status, backgroundColor: bgColor, color: fontColor}}>{props.status}</div>}
    </div>
  );
};

const styles = {
    container: {
        display: "flex",
        justifyContent: "space-between",
        fontWeight: 550,
        fontSize: 20,
        TextDecoration: "none",
        alignItems: "center",
    },
    status: {
        fontSize: 15,
        padding: "5px 15px",
        borderRadius: 30,
    }
} as const;

export default Task;
