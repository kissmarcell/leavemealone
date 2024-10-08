import Task from "@/components/project/Task";
import Colors from "@/constants/Colors";
import { IssueType } from "@/types/project";

type ProjectBodyProps = {
  issues: IssueType[];
};

const ProjectBody = (props: ProjectBodyProps) => {
  return (
    <div style={styles.backdropContainer}>
      <div style={styles.container}>
        {props.issues.map((issue) => (
          <Task name={issue.name} link={issue.url} tags={issue.tags} />
        ))}
      </div>
    </div>
  );
};

const styles = {
  backdropContainer: {
    backdropFilter: "blur(25px)",
    borderRadius: "0 0 25px 25px",
  },
  container: {
    display: "flex",
    flexDirection: "column",
    gap: "40px",
    color: Colors.black,
    backgroundColor: Colors.white,
    opacity: "0.4",
    borderRadius: "0 0 25px 25px",
    padding: "20px 40px",
  },
} as const;

export default ProjectBody;
