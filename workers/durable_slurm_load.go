type DurableContext interface {
    context.Context

    RetryCount() int64

    RunTask(ctx context.Context, taskName string, in []byte) (out []byte, err error)
}
