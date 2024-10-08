import Tag from "@/components/project/Tag";

type TaskProps = {
  name: string;
  link: string;
  tags?: string[];
};

const Task = (props: TaskProps) => {
  return (
    <div style={styles.container}>
      <a href={props.link} target="_blank">
        {props.name}
      </a>
      {props.tags && (
        <div style={styles.tagContainer}>
          {props.tags.map((tag) => (
            <Tag name={tag} />
          ))}
        </div>
      )}
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
  tagContainer: {
    display: "flex",
    gap: 10,
  },
} as const;

export default Task;
